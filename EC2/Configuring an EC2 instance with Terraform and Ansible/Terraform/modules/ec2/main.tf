resource "tls_private_key" "key-pair" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "key-pair" {
  key_name   = "${var.ec2_name}-key-pair"
  public_key = tls_private_key.key-pair.public_key_openssh
}
resource "local_file" "private_key" {
  content  = tls_private_key.key-pair.private_key_pem
  filename = "${path.module}/terraform-key.pem"
}
