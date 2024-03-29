resource "aws_ses_email_identity" "data_ops_email" {
  email = var.data_ops_email
}