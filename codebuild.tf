resource "aws_codebuild_source_credential" "automation_test_project" {
  auth_type   = "PERSONAL_ACCESS_TOKEN"
  server_type = "GITHUB_ENTERPRISE"
  token       = var.github_personal_token
}


resource "aws_codebuild_project" "integration_automation_test_project" {
  name          = "${local.prefix}-integration"
  description   = "integration test automation test codebuild project"
  build_timeout = "60"
  service_role  = aws_iam_role.codebuild_role.arn

  artifacts {
    type = "S3"
    location = aws_s3_bucket.data_mart_at_s3.bucket
    encryption_disabled = true
    override_artifact_name = true
  }

  environment {
    compute_type                = "BUILD_GENERAL1_SMALL"
    image                       = "aws/codebuild/standard:5.0"
    type                        = "LINUX_CONTAINER"
    image_pull_credentials_type = "CODEBUILD"

    environment_variable {
      name  = "S3_ATHENA_OUTPUT"
      value = aws_s3_bucket.data_mart_at_s3.bucket
    }

    environment_variable {
      name  = "SNOWFLAKE_SCHEMA"
      value = var.snowflake_schema
    }

    
    environment_variable {
      name  = "ENVIRONMENT"
      value = local.prefix
    }

    environment_variable {
      name  = "DATA_OPS_EMAIL"
      value = var.data_ops_email
    }
    
  }

  source {
    type            = "GITHUB_ENTERPRISE"
    location        = "https://github.com/lightningntt/data_test"
    git_clone_depth = 1
    buildspec       = "buildspec/buildspec-integration.yml"
  }

  source_version = "refs/heads/develop"

  tags = {
    Environment = "Test"
  }
}