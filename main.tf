terraform {

  backend "s3" {
    key            = "terraform.tfstate"
  }
}

provider "aws" {
  region = "${var.aws_region}"
}

locals {
  prefix = "${var.your_account}-${var.prefix_value}"

  account_id = data.aws_caller_identity.current.account_id
  region     = data.aws_region.current.name

  tags = {
    Type      = "Automation test"
  }
}

data "aws_region" "current" {}
data "aws_caller_identity" "current" {}