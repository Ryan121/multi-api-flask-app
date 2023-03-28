output "subnet_ids" {
  value = aws_subnet.app_subnets[*].id
}

output "availability_zones" {
  value = data.aws_availability_zones.availability_zones
}