from django.core.management.base import BaseCommand
from core.models import Executive


class Command(BaseCommand):
    help = 'Add sample executives to the database'

    def handle(self, *args, **options):
        # Clear existing executives
        Executive.objects.all().delete()

        # Add sample executives
        executives_data = [
            {
                'name': 'Comr. Abdullahi Ibrahim',
                'position': 'President',
                'school': 'Kogi State University, Anyigba',
                'phone_number': '+234 803 123 4567',
                'bio': 'A visionary leader committed to student welfare and academic excellence.',
                'order': 1
            },
            {
                'name': 'Comr. Blessing Ocholi',
                'position': 'Vice President',
                'school': 'Federal University Lokoja',
                'phone_number': '+234 805 234 5678',
                'bio': 'Dedicated to promoting unity and progress among Ankpa students.',
                'order': 2
            },
            {
                'name': 'Comr. Emmanuel Adah',
                'position': 'General Secretary',
                'school': 'University of Nigeria, Nsukka',
                'phone_number': '+234 807 345 6789',
                'bio': 'Efficient administrator ensuring smooth operations of the association.',
                'order': 3
            },
            {
                'name': 'Comr. Fatima Sule',
                'position': 'Financial Secretary',
                'school': 'Ahmadu Bello University, Zaria',
                'phone_number': '+234 809 456 7890',
                'bio': 'Transparent and accountable financial management.',
                'order': 4
            },
            {
                'name': 'Comr. Joseph Okpe',
                'position': 'Treasurer',
                'school': 'University of Abuja',
                'phone_number': '+234 811 567 8901',
                'bio': 'Prudent custodian of association funds.',
                'order': 5
            },
            {
                'name': 'Comr. Grace Ameh',
                'position': 'Public Relations Officer',
                'school': 'Federal Polytechnic Idah',
                'phone_number': '+234 813 678 9012',
                'bio': 'Bridging communication between members and the public.',
                'order': 6
            },
            {
                'name': 'Comr. David Ogwu',
                'position': 'Director of Socials',
                'school': 'Benue State University, Makurdi',
                'phone_number': '+234 815 789 0123',
                'bio': 'Organizing memorable events and social activities.',
                'order': 7
            },
            {
                'name': 'Comr. Mary Attah',
                'position': 'Welfare Director',
                'school': 'University of Jos',
                'phone_number': '+234 817 890 1234',
                'bio': 'Ensuring the welfare and well-being of all members.',
                'order': 8
            },
        ]

        for data in executives_data:
            Executive.objects.create(**data)

        self.stdout.write(
            self.style.SUCCESS(f'Successfully added {Executive.objects.count()} executives!')
        )
