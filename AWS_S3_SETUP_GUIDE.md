# AWS S3 Setup Guide for SHPE Website Media Files

This guide will help you set up AWS S3 for storing media files (like alumni headshots) on Heroku.

## Why S3?

Heroku uses an ephemeral filesystem, meaning any files uploaded to the server will be deleted when the dyno restarts (at least once every 24 hours). AWS S3 provides persistent, reliable cloud storage for user-uploaded media files.

---

## Step 1: Create an AWS Account

1. Go to [AWS Console](https://aws.amazon.com/)
2. Sign up for an AWS account (you'll need a credit card, but S3 storage is very cheap and has a generous free tier)

---

## Step 2: Create an S3 Bucket

1. Log into the [AWS Console](https://console.aws.amazon.com/)
2. Search for "S3" in the services search bar
3. Click "Create bucket"
4. Configure your bucket:
   - **Bucket name**: Choose a unique name (e.g., `shpe-uva-media-files`)
   - **AWS Region**: Choose a region close to you (e.g., `us-east-1`)
   - **Object Ownership**: Select "ACLs enabled" and "Object writer"
   - **Block Public Access settings**: **UNCHECK** "Block all public access" (we need public read access for images)
   - Acknowledge the warning about public access
5. Leave other settings as default
6. Click "Create bucket"

---

## Step 3: Create an IAM User with S3 Access

1. In AWS Console, search for "IAM" (Identity and Access Management)
2. Click "Users" in the left sidebar
3. Click "Create user"
4. **User name**: `shpe-website-s3-user`
5. Click "Next"
6. For permissions:
   - Select "Attach policies directly"
   - Search for and select `AmazonS3FullAccess`
7. Click "Next" then "Create user"

---

## Step 4: Create Access Keys

1. Click on the user you just created (`shpe-website-s3-user`)
2. Go to the "Security credentials" tab
3. Scroll down to "Access keys"
4. Click "Create access key"
5. Select "Application running outside AWS"
6. Click "Next" then "Create access key"
7. **IMPORTANT**: Copy both:
   - **Access key ID** (e.g., `AKIAIOSFODNN7EXAMPLE`)
   - **Secret access key** (e.g., `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`)
   
   ⚠️ You won't be able to see the secret key again, so save it somewhere secure!

---

## Step 5: Configure S3 Bucket CORS (Optional but Recommended)

1. Go back to S3 in the AWS Console
2. Click on your bucket name
3. Go to the "Permissions" tab
4. Scroll down to "Cross-origin resource sharing (CORS)"
5. Click "Edit" and paste this configuration:

```json
[
    {
        "AllowedHeaders": ["*"],
        "AllowedMethods": ["GET", "HEAD"],
        "AllowedOrigins": ["*"],
        "ExposeHeaders": []
    }
]
```

6. Click "Save changes"

---

## Step 6: Configure Heroku Environment Variables

Now you need to set environment variables in Heroku:

### Option A: Using Heroku CLI

```bash
heroku config:set USE_S3=True
heroku config:set AWS_ACCESS_KEY_ID=your_access_key_id_here
heroku config:set AWS_SECRET_ACCESS_KEY=your_secret_access_key_here
heroku config:set AWS_STORAGE_BUCKET_NAME=shpe-uva-media-files
heroku config:set AWS_S3_REGION_NAME=us-east-1
```

### Option B: Using Heroku Dashboard

1. Go to your app on [Heroku Dashboard](https://dashboard.heroku.com/)
2. Click on your app
3. Go to the "Settings" tab
4. Click "Reveal Config Vars"
5. Add the following variables:

| Key | Value |
|-----|-------|
| `USE_S3` | `True` |
| `AWS_ACCESS_KEY_ID` | Your Access Key ID from Step 4 |
| `AWS_SECRET_ACCESS_KEY` | Your Secret Access Key from Step 4 |
| `AWS_STORAGE_BUCKET_NAME` | Your bucket name (e.g., `shpe-uva-media-files`) |
| `AWS_S3_REGION_NAME` | Your region (e.g., `us-east-1`) |

---

## Step 7: Deploy Updated Code to Heroku

1. Make sure all changes are committed:
   ```bash
   git add .
   git commit -m "Add AWS S3 storage for media files"
   ```

2. Push to Heroku:
   ```bash
   git push heroku main
   ```
   (Replace `main` with your branch name if different)

3. Wait for the build to complete

---

## Step 8: Test the Setup

1. Go to your Django admin panel: `https://www.shpeatuva.com/admin/`
2. Try adding a new alumni entry with a headshot
3. The image should now upload successfully to S3!
4. Check your S3 bucket in AWS Console - you should see the uploaded image in the `alumni_photos/` folder

---

## Local Development

For local development, you don't need to use S3. The app will automatically use local file storage when `USE_S3` is not set or is `False`.

If you want to test S3 locally, create a `.env` file in your project root:

```env
USE_S3=True
AWS_ACCESS_KEY_ID=your_access_key_id_here
AWS_SECRET_ACCESS_KEY=your_secret_access_key_here
AWS_STORAGE_BUCKET_NAME=shpe-uva-media-files
AWS_S3_REGION_NAME=us-east-1
```

---

## Cost Estimate

AWS S3 pricing is very low:
- **Storage**: ~$0.023 per GB per month
- **Requests**: $0.005 per 1,000 GET requests
- **Data Transfer**: First 100GB/month out to internet is free

For a typical alumni directory with ~100 headshots (each ~50KB after compression), you're looking at:
- Storage: ~5MB = **$0.0001/month**
- Requests: Even with 10,000 page views/month = **$0.05/month**

**Total estimated cost: Less than $1/month**

AWS also offers a free tier:
- 5GB of storage
- 20,000 GET requests
- 2,000 PUT requests

So you'll likely stay within the free tier for a long time!

---

## Troubleshooting

### Images not loading?
- Check that your bucket's "Block Public Access" settings allow public reads
- Verify the `AWS_DEFAULT_ACL = 'public-read'` setting in `settings.py`
- Check the browser console for CORS errors

### Upload failing?
- Verify all environment variables are set correctly in Heroku
- Check IAM user has S3 permissions
- Look at Heroku logs: `heroku logs --tail`

### Wrong region?
- Make sure `AWS_S3_REGION_NAME` matches your bucket's region
- You can find your bucket's region in the S3 console

---

## Security Best Practices

1. **Never commit AWS credentials to Git** - Always use environment variables
2. **Use IAM user with minimal permissions** - Don't use your root AWS account
3. **Regularly rotate access keys** - Change them every 90 days
4. **Monitor S3 bucket access** - Enable CloudWatch logging if needed
5. **Consider using AWS Secrets Manager** for production apps with sensitive data

---

## Alternative: Cloudinary

If you prefer a simpler setup, consider [Cloudinary](https://cloudinary.com/) which has:
- Free tier: 25GB storage, 25GB bandwidth/month
- Built-in image transformations
- Simpler setup

To use Cloudinary instead:
1. Replace `django-storages` and `boto3` with `cloudinary` in `requirements.txt`
2. Update `settings.py` accordingly
3. No bucket creation needed - just sign up and get API credentials

---

## Questions?

If you run into issues, check:
- [Django Storages Documentation](https://django-storages.readthedocs.io/)
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/)
- [Heroku Config Vars](https://devcenter.heroku.com/articles/config-vars)



