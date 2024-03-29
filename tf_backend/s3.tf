resource "aws_s3_bucket" "terraform_state" {
  bucket = var.s3_lock
  lifecycle {
    prevent_destroy = true
  }
}


