
resource "aws_s3_bucket" "data_mart_at_s3" {
  bucket = "${local.prefix}-s3"
  tags   = local.tags
}

resource "aws_s3_bucket_public_access_block" "data_mart_at_s3" {
  bucket                  = aws_s3_bucket.data_mart_at_s3.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}