provider "aws" {
    region = "us-east-1"
}

terraform {
  
    # backend "local" {

    #     path = "relative/path/to/terraform.tfstate"

    # }

    backend "s3" {
    bucket         = "terraform-state-backend-k8s"
    key            = "terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform_state_k8s"
  }
#   backend "remote" {
    
#   }
  
  required_providers {
    
    aws = {
        source  = "hashicorp/aws"
        version = ">4.33.0"
    }
  }

}

/* Provision dyno_db table  and s3 backend via terraform when using a local remote backend  */

resource "aws_dynamodb_table" "terraform-lock" {
    name           = "terraform_state_k8s"
    read_capacity  = 5
    write_capacity = 5
    hash_key       = "LockID"
    attribute {
        name = "LockID"
        type = "S"
    }
    tags = {
        "Name" = "DynamoDB Terraform State Lock Table K8s"
    }
}

resource "aws_s3_bucket" "bucket" {
    bucket = "terraform-state-backend-k8s"
    versioning {
        enabled = true
    }
    server_side_encryption_configuration {
        rule {
            apply_server_side_encryption_by_default {
                sse_algorithm = "AES256"
            }
        }
    }
    object_lock_configuration {
        object_lock_enabled = "Enabled"
    }

}