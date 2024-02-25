import json
from django.core.management.base import BaseCommand
from thesis.models import Thesis, Comment


class Command(BaseCommand):
    help = 'Load data from data.json into the database'

    def handle(self, *args, **options):
        try:
            with open('data.json', 'r') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError as e:
                    self.stdout.write(self.style.ERROR(f"Invalid JSON format in data.json: {e}"))
                    return

                for item in data:
                    model_name = item.get('model', '')
                    fields = item.get('fields', {})
                    if model_name == 'thesis.thesis':
                        try:
                            thesis = Thesis.objects.create(
                                title=fields['title'],
                                author=fields['author'],
                                abstract=fields['abstract'],
                                year=fields['year']
                            )
                            self.stdout.write(self.style.SUCCESS(f"Created thesis: {thesis.title}"))
                        except KeyError as e:
                            self.stdout.write(self.style.ERROR(f"Missing field in thesis data: {e}"))
                    elif model_name == 'thesis.comment':
                        try:
                            thesis_id = fields.pop('thesis')
                            thesis = Thesis.objects.get(pk=thesis_id)
                            comment = Comment.objects.create(thesis=thesis, **fields)
                            self.stdout.write(self.style.SUCCESS(f"Created comment on {thesis.title}: {comment.text}"))
                        except (Thesis.DoesNotExist, KeyError) as e:
                            self.stdout.write(self.style.ERROR(f"Error creating comment: {e}"))
                    else:
                        self.stdout.write(self.style.ERROR(f"Unknown model type: {model_name}"))

                self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('data.json file not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {str(e)}"))
