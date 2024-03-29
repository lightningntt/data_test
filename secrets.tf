data "aws_secretsmanager_secret_version" "ghe_personal_token" {
  secret_id = "ghe-personal-token"
}
