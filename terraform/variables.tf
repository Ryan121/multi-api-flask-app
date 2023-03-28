variable "eks_cluster_name" {
  description = "The name of the EKS Cluster"
  default     = "api-eks"
}

variable "availability_zones" {
  description = "Availability zones"
  type        = list(string)
  default     = ["us-east-1a", "us-east-1b"]
}