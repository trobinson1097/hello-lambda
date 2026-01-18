output "s3_bucket_name" {
  description = "The name of the S3 bucket for Lambda deployment packages."
  value       = aws_s3_bucket.lambda_bucket.id
}
