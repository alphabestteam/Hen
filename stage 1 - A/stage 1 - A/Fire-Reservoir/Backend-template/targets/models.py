from django.db import models

class Target(models.Model):
    name = models.CharField(max_length=20)
    attack_priority = models.IntegerField()
    latitude = models.DecimalField(max_digits=33, decimal_places=30)
    longitude = models.DecimalField(max_digits=33, decimal_places=30)
    enemy_organization = models.CharField(max_length=20)
    target_goal = models.CharField(max_length=30)
    target_id = models.IntegerField(primary_key=True)
    was_target_destroyed = models.BooleanField()

def _str_(self):
    return f"target name:{self.target_name}, prioritize: {self.prioritize}, target_coordinates_width: {self.target_coordinates_width},  target_coordinates_length: {self.target_coordinates_length}, enemy_organization: {self.enemy_organization}, purpose_designation: {self.purpose_designation},target_attacked: {self.target_attacked}, id_target: {self.id_target}"
