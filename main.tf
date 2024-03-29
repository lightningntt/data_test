terraform {

  backend "s3" {
    key            = "terraform.tfstate"
  }
}

provider "aws" {
  region = "${var.aws_region}"
}

locals {
  prefix = "${var.prefix_value}"

  account_id = data.aws_caller_identity.current.account_id
  region     = data.aws_region.current.name

  tags = {
    Type      = "Automation test"
  }

  ghe_personal_token = jsondecode(
    data.aws_secretsmanager_secret_version.ghe_personal_token.secret_string
  )
}
data "aws_region" "current" {}
data "aws_caller_identity" "current" {}
data "aws_iam_account_alias" "current" {}
