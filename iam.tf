
resource "aws_iam_role" "codebuild_role" {
  name                     = "${local.prefix}-codebuild"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "codebuild.amazonaws.com"
        }
      },
    ]
  })
}

resource "aws_iam_role_policy" "codebuild_policy" {
  name = "${local.prefix}-codebuild-policy"
  role = aws_iam_role.codebuild_role.name

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Resource": [
                "arn:aws:logs:${local.region}:${local.account_id}:log-group:/aws/codebuild/*"
            ],
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ]
        },
        {
            "Effect": "Allow",
            "Resource": [
                "arn:aws:s3:::codepipeline-*"
            ],
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:GetObjectVersion",
                "s3:GetBucketAcl",
                "s3:GetBucketLocation"
            ]
        },
        {
            "Effect": "Allow",
            "Resource": [
                "${aws_s3_bucket.data_mart_at_s3.arn}",
                "${aws_s3_bucket.data_mart_at_s3.arn}/*"
            ],
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:GetObjectVersion",
                "s3:GetBucketAcl",
                "s3:GetBucketLocation"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "codebuild:CreateReportGroup",
                "codebuild:CreateReport",
                "codebuild:UpdateReport",
                "codebuild:BatchPutTestCases",
                "codebuild:BatchPutCodeCoverages"
            ],
            "Resource": [
                "arn:aws:codebuild:${local.region}:${local.account_id}:report-group/*"
            ]
        },
        {
            "Effect": "Allow",
            "Resource": [
                "*"
            ],
            "Action": [
                "s3:ListBucket",
                "lambda:GetFunctionConfiguration",
                "logs:ListTagsLogGroup",
                "events:DescribeRule",
                "ses:SendRawEmail",
                "secretsmanager:GetSecretValue"
            ]
        }
    ]
}
EOF
}

resource "aws_iam_role" "trigger_codebuild_role" {
  name                     = "${local.prefix}-cloudwatch-trigger-codebuild"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "events.amazonaws.com"
        }
      },
    ]
  })
}

resource "aws_iam_role_policy" "trigger_codebuild_policy" {
  name = "${local.prefix}-trigger-codebuild-policy"
  role = aws_iam_role.trigger_codebuild_role.name

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "codebuild:StartBuild"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
EOF
}