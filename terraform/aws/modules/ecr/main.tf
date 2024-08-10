resource "aws_ecr_repository" "ecr" {
    name = var.repository_name
    image_tag_mutability = var.image_tag_mutability
    force_delete = var.force_delete

    image_scanning_configuration {
        scan_on_push = var.scan_on_push
    }

    # Adding tags
    tags = var.tags
}