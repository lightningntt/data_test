variable "lambda_config" {
  type = object({
    runtime                  = string
    compatible_architectures = string
    default_timeout          = number
  })
  default = {
    runtime                  = "python3.8"
    compatible_architectures = "x86_64"
    default_timeout          = 900
  }
}


variable "prefix_value" {
  type    = string
}

variable "snowflake_schema" {
  type    = string
}

variable "aws_region" {
  type    = string
}

variable "data_ops_email" {
  type    = string
}

variable "source_version" {
  type    = string
}

variable "github_personal_token" {
  type    = string
}

variable "your_account" {
  type = string
}

variable "your_repo" {
  type = string
}