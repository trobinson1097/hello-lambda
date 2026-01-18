variable "aws_region" {
  description = "AWS region to deploy resources into"
  type        = string
  default     = "us-east-2"
}

variable "s3_bucket" {
  description = "unique s3 bucket name"
  type        = string
  default     = "rebecca-parker-bucket-cloud2-lambda"
}