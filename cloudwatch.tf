resource "aws_cloudwatch_event_rule" "integration_codebuild_trigger" {
    name = "${local.prefix}-integration-trigger"
    description = "scheduler-event"
    schedule_expression = "cron(0 12 ? * SUN *)"
}

resource "aws_cloudwatch_event_target" "integration_codebuild_trigger" {
  rule      = aws_cloudwatch_event_rule.integration_codebuild_trigger.name
  arn       = aws_codebuild_project.integration_automation_test_project.arn
  role_arn  = aws_iam_role.trigger_codebuild_role.arn
  input = <<JSON
        {
        "environmentVariablesOverride": [{
            "name": "TRIGGER_START_BUILD",
            "type": "PLAINTEXT",
            "value": "This trigger be requested from cloudwatch eventbridge"
        }]
        }
        JSON
}
