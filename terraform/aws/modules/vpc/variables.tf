variable "cidr_block" {
  type = string
  default = null
}

variable "enable_dns_support" {
  type = bool
  default = null
}

variable "enable_dns_hostnames" {
  type = bool
  default = null
}

variable "tags" {
  type = map(string)
  default = null
}