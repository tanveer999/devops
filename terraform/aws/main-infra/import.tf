##############################################################
## tf import 
## tf import aws_vpc.this <vpc_id>

# resource "aws_vpc" "this" {
#   cidr_block = "172.16.0.0/16"
#   enable_dns_hostnames = true
#   enable_dns_support = true
#   tags = {
#     Name = "test"
#   }
# }

##############################################################

## tf import module.vpc.aws_vpc.this <vpc_id>

# module "vpc" {
#   source = "../modules/vpc"
  
# }

#############################################################

## tf import module.vpc[\"test\"].aws_vpc.this <vpc_id>

# module "vpc" {
#   source = "../modules/vpc"

#   for_each = var.vpc_config
# }

# variable "vpc_config" {
#   default = {
#     test = {
#     }
#   }
# }

##############################################################

## Using import block

import {
    for_each = var.vpc_config
    to = module.vpc[each.key].aws_vpc.this
    id = each.value.id
}

module "vpc" {
  source = "../modules/vpc"

  for_each = var.vpc_config
  tags = try(each.value.tags, null)
}

variable "vpc_config" {
  default = {
    test = {
        id = "vpc-029e094861e3ca8a6"
        tags = {
          Name = "test"
        }
    }
  }
}