module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "my-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["ap-south-1a"]
  private_subnets = ["10.0.1.0/24"]
  # private_subnet_suffix = "aklsfjfklafaslfj"
  public_subnet_names = ["axis-videopd-cicd-public-subnet-1a"]
  public_subnets  = ["10.0.101.0/24"]

  enable_nat_gateway = false
  enable_vpn_gateway = false

  tags = {
    Terraform = "true"
    Environment = "dev"
  }
}