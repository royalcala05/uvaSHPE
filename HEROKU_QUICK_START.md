# Quick Start: Fixing the Media Upload Error

## The Problem
You're getting this error when trying to upload images in Django admin:
```
OSError: [Errno 30] Read-only file system: '/media'
```

This happens because Heroku's filesystem is read-only and ephemeral. You need to use cloud storage (AWS S3).

---

## Quick Fix Steps

### 1. Set up AWS S3 (One-time setup)
Follow the complete guide in `AWS_S3_SETUP_GUIDE.md` to:
- Create an S3 bucket
- Create an IAM user
- Get your AWS credentials

### 2. Set Heroku Environment Variables

Once you have your AWS credentials, run these commands:

```bash
heroku config:set USE_S3=True
heroku config:set AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
heroku config:set AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
heroku config:set AWS_STORAGE_BUCKET_NAME=shpe-uva-media-files
heroku config:set AWS_S3_REGION_NAME=us-east-1
```

Replace the values with your actual:
- AWS Access Key ID
- AWS Secret Access Key  
- S3 Bucket Name
- AWS Region

### 3. Deploy the Updated Code

```bash
# Navigate to your project directory
cd uvaSHPE/shpe_website

# Commit the changes
git add .
git commit -m "Add AWS S3 storage for media files"

# Push to Heroku
git push heroku main
```

### 4. Verify Config Vars

Check that all variables are set:
```bash
heroku config
```

You should see all five variables listed above.

---

## Testing

1. Go to: `https://www.shpeatuva.com/admin/website/alumni/add/`
2. Upload a headshot image
3. Save the alumni entry
4. It should work! ✅

---

## Need Help?

See the complete setup guide: `AWS_S3_SETUP_GUIDE.md`



