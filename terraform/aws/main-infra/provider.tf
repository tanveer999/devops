terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.49.0"
    }
  }
}

provider "aws" {
  # Configuration options
  region = "ap-south-1"
  default_tags {
    tags = {
      managed_by = "terraform"
    }
  }
}