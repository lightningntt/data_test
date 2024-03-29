resource "aws_dynamodb_table" "terraform_locks" {
  name           = var.dynamodb_lock
  read_capacity  = 1
  write_capacity = 1
  hash_key       = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}