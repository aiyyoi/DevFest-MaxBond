from django.db import models
# from django.contrib.auth.models import User


class language_info(models.Model):
	name = models.CharField(max_length=255, unique=True)


class basic_base(models.Model):
	GENDER_CHOICES = (('1','male'),('2','female'),('9','not applicable'))
	MARITAL_STATUS_CHOICES = (('1','single'),('2','married')) 
	BLOOD_TYPE_CHOICES = (('1','A'),('2','B'),('3','AB'),('4','O'))
	IMPORTANCE_SCORE_CHOICES = (('1',1),('2',2),('3',3),('4',4),('5',5))
	FAMILARITY_SCORE_CHOICES = (('1',1),('2',2),('3',3),('4',4),('5',5))

	owner_id = models.IntegerField(null=True)
	person_id = models.IntegerField(null=True)
	prefix = models.CharField(max_length=255, blank=True)
	first_name = models.CharField(max_length=255, blank=True)
	middle_name = models.CharField(max_length=255, blank=True)
	last_name = models.CharField(max_length=255, blank=True)
	suffix = models.CharField(max_length=255, blank=True)
	nickname = models.CharField(max_length=255, blank=True)
	gender = models.CharField(max_length=1, blank=True, choices=GENDER_CHOICES)
	birthday = models.DateField(blank=True, null=True)
	age = models.IntegerField(blank=True, null=True)
	photo = models.ImageField("Profile pic", upload_to="images/", blank=True, null=True)
	marital_status = models.CharField(max_length=1, blank=True, choices=MARITAL_STATUS_CHOICES)
	blood_type = models.CharField(max_length=1, blank=True, choices=BLOOD_TYPE_CHOICES)
	importance_score = models.CharField(max_length=1, blank=True, choices=IMPORTANCE_SCORE_CHOICES)
	familarity_score = models.CharField(max_length=1, blank=True, choices=FAMILARITY_SCORE_CHOICES)
	core_relation_with_me = models.CharField(max_length=255, blank=True)
	how_many_years = models.IntegerField(null=True, blank=True)
	fk_languages = models.ManyToManyField(language_info)


class note_info(models.Model):
	note_content = models.TextField()


class interest_skill_info(models.Model):
	name = models.CharField(max_length=255, unique=True)


class industry_info(models.Model):
	name = models.CharField(max_length=255, unique=True)


class company_info(models.Model):
	name = models.CharField(max_length=255, unique=True)
	fk_industry_id = models.ForeignKey(industry_info)


class position_info(models.Model):
	name = models.CharField(max_length=255, unique=True)


class country_info(models.Model):
	name = models.CharField(max_length=255, unique=True)


class states_info(models.Model):
	name = models.CharField(max_length=255, unique=True)
	fk_country_id = models.ForeignKey(country_info)


class cities_info(models.Model):
	name = models.CharField(max_length=255, unique=True)
	fk_state_id = models.ForeignKey(states_info)


class location_info(models.Model):
	name = models.CharField(max_length=255, unique=True)
	fk_country_id = models.ForeignKey(country_info)
	fk_state_id = models.ForeignKey(states_info)
	fk_city_id = models.ForeignKey(cities_info)


class location_item_name_info(models.Model):
	name = models.CharField(max_length=255, unique=True)


class school_info(models.Model):
	name = models.CharField(max_length=255, unique=True)


class concentration_info(models.Model):
	name = models.CharField(max_length=255, unique=True)


class degree_info(models.Model):
	name = models.CharField(max_length=255, unique=True)


class phone_item_name_info(models.Model):
	name = models.CharField(max_length=255, unique=True)


class email_item_name_info(models.Model):
	name = models.CharField(max_length=255, unique=True)


class sn_item_name_info(models.Model):
	name = models.CharField(max_length=255, unique=True)


class phone_number_info(models.Model):
	number = models.BigIntegerField(blank=True, null=True)
	fk_item_name_id = models.ForeignKey(phone_item_name_info)


class email_info(models.Model):
	email_address = models.EmailField(blank=True)
	fk_item_name_id = models.ForeignKey(email_item_name_info)


class sn_info(models.Model):
	sn_username = models.CharField(max_length=255, unique=True)
	sn_url = models.CharField(max_length=255, unique=True)
	fk_item_name_id = models.ForeignKey(sn_item_name_info)


class has_phone_number_info(models.Model):
	fk_basic_base_id = models.ForeignKey(basic_base)
	fk_phone_number_id = models.ForeignKey(phone_number_info)


class has_email_info(models.Model):
	fk_basic_base_id = models.ForeignKey(basic_base)
	fk_email_id = models.ForeignKey(email_info)


class has_sn_info(models.Model):
	fk_basic_base_id = models.ForeignKey(basic_base)
	fk_sn_id = models.ForeignKey(sn_info)


class has_interest_skill(models.Model):
	LEVEL_CHOICES = (('1',1),('2',2),('3',3),('4',4),('5',5))

	level = models.CharField(max_length=1, blank=True, choices=LEVEL_CHOICES)
	fk_basic_base_id = models.ForeignKey(basic_base)
	fk_interest_skill_id = models.ForeignKey(interest_skill_info)


class has_note(models.Model):
	CATEGORY_CHOICES = (('1','work'),('2','school'),('3','interest/skill'),('4','other'))

	category = models.CharField(max_length=1, default='4', blank=True, choices=CATEGORY_CHOICES)
	note_date = models.DateField(auto_now_add=True)
	reminder_date = models.DateTimeField(blank=True, null=True)
	fk_note_id = models.ForeignKey(note_info)
	fk_basic_base_id = models.ForeignKey(basic_base)


class work_for(models.Model):
	start_date = models.DateField(blank=True, null=True)
	end_date = models.DateField(blank=True, null=True)
	fk_basic_base_id = models.ForeignKey(basic_base)
	fk_position_id = models.ForeignKey(position_info)
	fk_company_id = models.ForeignKey(company_info)
	fk_location_id = models.ForeignKey(location_info)


class go_location(models.Model):
	fk_basic_base_id = models.ForeignKey(basic_base)
	fk_location_id = models.ForeignKey(location_info)
	fk_location_item_name_id = models.ForeignKey(location_item_name_info)


class we_meet(models.Model):
	how_or_who = models.CharField(max_length=255, blank=True)
	note = models.TextField(blank=True)
	when = models.DateField(blank=True)
	fk_basic_base_id = models.ForeignKey(basic_base)
	fk_location_id = models.ForeignKey(location_info)


class has_edu(models.Model):
	class_year = models.IntegerField(null=True, blank=True)
	fk_basic_base_id = models.ForeignKey(basic_base)
	fk_concentration_id = models.ForeignKey(concentration_info)
	fk_degree_id = models.ForeignKey(degree_info)
	fk_school_id = models.ForeignKey(school_info)
	fk_location_id = models.ForeignKey(location_info)