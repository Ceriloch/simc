#!/usr/bin/env python3

output = """
deathknight="PR_Death_Knight_Frost_2H"
source=default
spec=frost
level=60
race=orc
role=attack
position=back
talents=1221212

# Default consumables
potion=potion_of_unbridled_fury
flask=greater_flask_of_the_undertow
food=abyssalfried_rissole
augmentation=battle_scarred

# Executed before combat begins. Accepts non-harmful actions only.
actions.precombat=flask
actions.precombat+=/food
actions.precombat+=/augmentation
# Snapshot raid buffed stats before combat begins and pre-potting is done.
actions.precombat+=/snapshot_stats
actions.precombat+=/potion
actions.precombat+=/raise_dead
# actions.precombat+=/variable,name=other_on_use_equipped,value=

# Executed every time the actor is available.
actions=auto_attack
# Apply Frost Fever and maintain Icy Talons
actions+=/howling_blast,if=!dot.frost_fever.ticking&(!talent.breath_of_sindragosa.enabled|cooldown.breath_of_sindragosa.remains>15)
actions+=/glacial_advance,if=buff.icy_talons.remains<=gcd&buff.icy_talons.up&spell_targets.glacial_advance>=2&(!talent.breath_of_sindragosa.enabled|cooldown.breath_of_sindragosa.remains>15)
actions+=/frost_strike,if=buff.icy_talons.remains<=gcd&buff.icy_talons.up&(!talent.breath_of_sindragosa.enabled|cooldown.breath_of_sindragosa.remains>15)
actions+=/use_items
actions+=/potion,if=buff.pillar_of_frost.up&buff.empower_rune_weapon.up
# Action List Calls
actions+=/call_action_list,name=cooldowns
actions+=/call_action_list,name=cold_heart,if=talent.cold_heart.enabled&((buff.cold_heart.stack>=10&debuff.razorice.stack=5)|target.1.time_to_die<=gcd)
actions+=/run_action_list,name=bos_ticking,if=buff.breath_of_sindragosa.up
actions+=/run_action_list,name=bos_pooling,if=talent.breath_of_sindragosa.enabled&((cooldown.breath_of_sindragosa.remains=0&cooldown.pillar_of_frost.remains<10)|(cooldown.breath_of_sindragosa.remains<20&target.1.time_to_die<35))
actions+=/run_action_list,name=obliteration,if=buff.pillar_of_frost.up&talent.obliteration.enabled
actions+=/run_action_list,name=aoe,if=active_enemies>=2
actions+=/call_action_list,name=standard
# Racial Abilities
actions+=/blood_fury,if=buff.pillar_of_frost.up&buff.empower_rune_weapon.up
actions+=/berserking,if=buff.pillar_of_frost.up
actions+=/arcane_pulse,if=(!buff.pillar_of_frost.up&active_enemies>=2)|!buff.pillar_of_frost.up&(rune.deficit>=5&runic_power.deficit>=60)
actions+=/lights_judgment,if=buff.pillar_of_frost.up
actions+=/ancestral_call,if=buff.pillar_of_frost.up&buff.empower_rune_weapon.up
actions+=/fireblood,if=buff.pillar_of_frost.remains<=8&buff.empower_rune_weapon.up
actions+=/bag_of_tricks,if=buff.pillar_of_frost.up&(buff.pillar_of_frost.remains<5&talent.cold_heart.enabled|!talent.cold_heart.enabled&buff.pillar_of_frost.remains<3)&active_enemies=1|buff.seething_rage.up&active_enemies=1

# AoE Rotation
actions.aoe=remorseless_winter,if=talent.gathering_storm.enabled
actions.aoe+=/glacial_advance,if=talent.frostscythe.enabled
actions.aoe+=/frost_strike,target_if=(debuff.razorice.stack<5|debuff.razorice.remains<10)&cooldown.remorseless_winter.remains<=2*gcd&talent.gathering_storm.enabled&!talent.frostscythe.enabled
actions.aoe+=/frost_strike,if=cooldown.remorseless_winter.remains<=2*gcd&talent.gathering_storm.enabled
actions.aoe+=/howling_blast,if=buff.rime.up
actions.aoe+=/frostscythe,if=buff.killing_machine.up
actions.aoe+=/glacial_advance,if=runic_power.deficit<(15+talent.runic_attenuation.enabled*3)
actions.aoe+=/frost_strike,target_if=(debuff.razorice.stack<5|debuff.razorice.remains<10)&runic_power.deficit<(15+talent.runic_attenuation.enabled*3)&!talent.frostscythe.enabled
actions.aoe+=/frost_strike,if=runic_power.deficit<(15+talent.runic_attenuation.enabled*3)&!talent.frostscythe.enabled
actions.aoe+=/remorseless_winter
actions.aoe+=/frostscythe
actions.aoe+=/obliterate,target_if=(debuff.razorice.stack<5|debuff.razorice.remains<10)&runic_power.deficit>(25+talent.runic_attenuation.enabled*3)&!talent.frostscythe.enabled
actions.aoe+=/obliterate,if=runic_power.deficit>(25+talent.runic_attenuation.enabled*3)
actions.aoe+=/glacial_advance
actions.aoe+=/frost_strike,target_if=(debuff.razorice.stack<5|debuff.razorice.remains<10)&!talent.frostscythe.enabled
actions.aoe+=/frost_strike
actions.aoe+=/horn_of_winter
actions.aoe+=/arcane_torrent

# Breath of Sindragosa pooling rotation : starts 20s before Pillar of Frost + BoS are available
actions.bos_pooling=howling_blast,if=buff.rime.up
actions.bos_pooling+=/obliterate,target_if=(debuff.razorice.stack<5|debuff.razorice.remains<10)&&runic_power.deficit>=25&!talent.frostscythe.enabled
actions.bos_pooling+=/obliterate,if=runic_power.deficit>=25
actions.bos_pooling+=/glacial_advance,if=runic_power.deficit<20&spell_targets.glacial_advance>=2&cooldown.pillar_of_frost.remains>5
actions.bos_pooling+=/frost_strike,target_if=(debuff.razorice.stack<5|debuff.razorice.remains<10)&runic_power.deficit<20&!talent.frostscythe.enabled&cooldown.pillar_of_frost.remains>5
actions.bos_pooling+=/frost_strike,if=runic_power.deficit<20&cooldown.pillar_of_frost.remains>5
actions.bos_pooling+=/frostscythe,if=buff.killing_machine.up&runic_power.deficit>(15+talent.runic_attenuation.enabled*3)&spell_targets.frostscythe>=2
actions.bos_pooling+=/frostscythe,if=runic_power.deficit>=(35+talent.runic_attenuation.enabled*3)&spell_targets.frostscythe>=2
actions.bos_pooling+=/obliterate,target_if=(debuff.razorice.stack<5|debuff.razorice.remains<10)&runic_power.deficit>=(35+talent.runic_attenuation.enabled*3)&!talent.frostscythe.enabled
actions.bos_pooling+=/obliterate,if=runic_power.deficit>=(35+talent.runic_attenuation.enabled*3)
actions.bos_pooling+=/glacial_advance,if=cooldown.pillar_of_frost.remains>rune.time_to_4&runic_power.deficit<40&spell_targets.glacial_advance>=2
actions.bos_pooling+=/frost_strike,target_if=(debuff.razorice.stack<5|debuff.razorice.remains<10)&cooldown.pillar_of_frost.remains>rune.time_to_4&runic_power.deficit<40&!talent.frostscythe.enabled
actions.bos_pooling+=/frost_strike,if=cooldown.pillar_of_frost.remains>rune.time_to_4&runic_power.deficit<40

# Breath of Sindragosa Ticking Rotation
actions.bos_ticking=obliterate,target_if=(debuff.razorice.stack<5|debuff.razorice.remains<10)&runic_power<=32&!talent.frostscythe.enabled
actions.bos_ticking+=/obliterate,if=runic_power<=32
actions.bos_ticking+=/remorseless_winter,if=talent.gathering_storm.enabled
actions.bos_ticking+=/howling_blast,if=buff.rime.up
actions.bos_ticking+=/obliterate,target_if=(debuff.razorice.stack<5|debuff.razorice.remains<10)&rune.time_to_5<gcd|runic_power<=45&!talent.frostscythe.enabled
actions.bos_ticking+=/obliterate,if=rune.time_to_5<gcd|runic_power<=45
actions.bos_ticking+=/frostscythe,if=buff.killing_machine.up&spell_targets.frostscythe>=2
actions.bos_ticking+=/horn_of_winter,if=runic_power.deficit>=32&rune.time_to_3>gcd
actions.bos_ticking+=/remorseless_winter
actions.bos_ticking+=/frostscythe,if=spell_targets.frostscythe>=2
actions.bos_ticking+=/obliterate,target_if=(debuff.razorice.stack<5|debuff.razorice.remains<10)&runic_power.deficit>25|rune>3&!talent.frostscythe.enabled
actions.bos_ticking+=/obliterate,if=runic_power.deficit>25|rune>3
actions.bos_ticking+=/arcane_torrent,if=runic_power.deficit>50

# Cold heart conditions
actions.cold_heart=chains_of_ice,if=buff.cold_heart.stack>5&target.1.time_to_die<gcd|buff.pillar_of_frost.remains<3


# Frost cooldowns
actions.cooldowns=pillar_of_frost,if=(cooldown.empower_rune_weapon.remains|talent.icecap.enabled)&!buff.pillar_of_frost.up
actions.cooldowns+=/breath_of_sindragosa,use_off_gcd=1,if=cooldown.empower_rune_weapon.remains&cooldown.pillar_of_frost.remains
actions.cooldowns+=/empower_rune_weapon,if=cooldown.pillar_of_frost.ready&talent.obliteration.enabled&rune.time_to_5>gcd&runic_power.deficit>=10|target.1.time_to_die<20
actions.cooldowns+=/empower_rune_weapon,if=(cooldown.pillar_of_frost.ready|target.1.time_to_die<20)&talent.breath_of_sindragosa.enabled&runic_power>60
actions.cooldowns+=/empower_rune_weapon,if=talent.icecap.enabled&rune<3
actions.cooldowns+=/frostwyrms_fury,if=buff.pillar_of_frost.remains<(3+talent.cold_heart.enabled*1)
actions.cooldowns+=/frostwyrms_fury,if=active_enemies>=2&cooldown.pillar_of_frost.remains+15>target.time_to_die|target.1.time_to_die<gcd
actions.cooldowns+=/raise_dead
#actions.cooldowns+=/sacrificial_pact,if=(buff.pillar_of_frost.up&buff.pillar_of_frost.remains=<1|cooldown.raise_dead.remains<63)&pet.ghoul_pet.active


# Obliteration rotation
actions.obliteration=remorseless_winter,if=talent.gathering_storm.enabled
actions.obliteration+=/obliterate,target_if=(debuff.razorice.stack<5|debuff.razorice.remains<10)&!talent.frostscythe.enabled&!buff.rime.up&spell_targets.howling_blast>=3
actions.obliteration+=/obliterate,if=!talent.frostscythe.enabled&!buff.rime.up&spell_targets.howling_blast>=3
actions.obliteration+=/frostscythe,if=(buff.killing_machine.react|(buff.killing_machine.up&(prev_gcd.1.frost_strike|prev_gcd.1.howling_blast|prev_gcd.1.glacial_advance)))&spell_targets.frostscythe>=2
actions.obliteration+=/obliterate,target_if=(debuff.razorice.stack<5|debuff.razorice.remains<10)&buff.killing_machine.react|(buff.killing_machine.up&(prev_gcd.1.frost_strike|prev_gcd.1.howling_blast|prev_gcd.1.glacial_advance))
actions.obliteration+=/obliterate,if=buff.killing_machine.react|(buff.killing_machine.up&(prev_gcd.1.frost_strike|prev_gcd.1.howling_blast|prev_gcd.1.glacial_advance))
actions.obliteration+=/glacial_advance,if=(!buff.rime.up|runic_power.deficit<10|rune.time_to_2>gcd)&spell_targets.glacial_advance>=2
actions.obliteration+=/howling_blast,if=buff.rime.up&spell_targets.howling_blast>=2
actions.obliteration+=/frost_strike,target_if=(debuff.razorice.stack<5|debuff.razorice.remains<10)&!buff.rime.up|runic_power.deficit<10|rune.time_to_2>gcd&!talent.frostscythe.enabled
actions.obliteration+=/frost_strike,if=!buff.rime.up|runic_power.deficit<10|rune.time_to_2>gcd
actions.obliteration+=/howling_blast,if=buff.rime.up
actions.obliteration+=/obliterate,target_if=(debuff.razorice.stack<5|debuff.razorice.remains<10)&!talent.frostscythe.enabled
actions.obliteration+=/obliterate

# Standard single-target rotation
actions.standard=remorseless_winter
actions.standard+=/frost_strike,if=cooldown.remorseless_winter.remains<=2*gcd&talent.gathering_storm.enabled
actions.standard+=/howling_blast,if=buff.rime.up
actions.standard+=/obliterate,if=!buff.frozen_pulse.up&talent.frozen_pulse.enabled
actions.standard+=/frost_strike,if=runic_power.deficit<(15+talent.runic_attenuation.enabled*3)
actions.standard+=/frostscythe,if=buff.killing_machine.up&rune.time_to_4>=gcd
actions.standard+=/obliterate,if=runic_power.deficit>(25+talent.runic_attenuation.enabled*3)
actions.standard+=/frost_strike
actions.standard+=/horn_of_winter
actions.standard+=/arcane_torrent

head=,id=178777,bonus_id=1500
neck=,id=178827,bonus_id=1500
shoulders=,id=178820,bonus_id=1500
back=,id=178851,bonus_id=1500
chest=,id=180099,bonus_id=1500
wrists=,id=179354,bonus_id=1500
hands=,id=178840,bonus_id=1500
waist=,id=178842,bonus_id=1500
legs=,id=178818,bonus_id=1500
feet=,id=180101,bonus_id=1500
finger1=,id=178933,bonus_id=1500
finger2=,id=178736,bonus_id=1500
trinket1=,id=178769,bonus_id=1500
trinket2=,id=179342,bonus_id=1500
main_hand=,id=178780,bonus_id=1500,enchant=rune_of_the_fallen_crusader
"""

def output_ilvl(ilvl):
    output = ""
    output += "profileset.{}_2h=talents=1221212\n".format(ilvl)
    output += "profileset.{}_2h+=head=,id=178777,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h+=neck=,id=178827,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h+=shoulders=,id=178820,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h+=back=,id=178851,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h+=chest=,id=180099,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h+=wrists=,id=179354,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h+=legs=,id=178818,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h+=feet=,id=180101,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h+=finger1=,id=178933,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h+=finger2=,id=178736,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h+=trinket1=,id=178769,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h+=trinket2=,id=179342,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h+=main_hand=,id=178780,ilevel={},enchant=rune_of_the_fallen_crusader\n".format(ilvl, ilvl)
    output += "\n"

    output += "profileset.{}_2h_fsc=talents=1223212\n".format(ilvl)
    output += "profileset.{}_2h_fsc+=head=,id=178777,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_fsc+=neck=,id=178827,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_fsc+=shoulders=,id=178820,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_fsc+=back=,id=178851,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_fsc+=chest=,id=180099,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_fsc+=wrists=,id=179354,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_fsc+=legs=,id=178818,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_fsc+=feet=,id=180101,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_fsc+=finger1=,id=178933,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_fsc+=finger2=,id=178736,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_fsc+=trinket1=,id=178769,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_fsc+=trinket2=,id=179342,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_fsc+=main_hand=,id=178780,ilevel={},enchant=rune_of_the_fallen_crusader\n".format(ilvl, ilvl)
    output += "\n"

    output += "profileset.{}_2h_bos=talents=2223213\n".format(ilvl)
    output += "profileset.{}_2h_bos+=head=,id=178777,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_bos+=neck=,id=178827,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_bos+=shoulders=,id=178820,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_bos+=back=,id=178851,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_bos+=chest=,id=180099,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_bos+=wrists=,id=179354,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_bos+=legs=,id=178818,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_bos+=feet=,id=180101,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_bos+=finger1=,id=178933,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_bos+=finger2=,id=178736,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_bos+=trinket1=,id=178769,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_bos+=trinket2=,id=179342,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_2h_bos+=main_hand=,id=178780,ilevel={},enchant=rune_of_the_fallen_crusader\n".format(ilvl, ilvl)
    output += "\n"

    output += "profileset.{}_dw=talents=1221212\n".format(ilvl)
    output += "profileset.{}_dw+=head=,id=178777,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw+=neck=,id=178827,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw+=shoulders=,id=178820,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw+=back=,id=178851,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw+=chest=,id=180099,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw+=wrists=,id=179354,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw+=legs=,id=178818,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw+=feet=,id=180101,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw+=finger1=,id=178933,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw+=finger2=,id=178736,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw+=trinket1=,id=178769,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw+=trinket2=,id=179342,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw+=main_hand=,id=178730,ilevel={},enchant=rune_of_razorice\n".format(ilvl, ilvl)
    output += "profileset.{}_dw+=off_hand=,id=179340,ilevel={},enchant=rune_of_the_fallen_crusader\n".format(ilvl, ilvl)
    output += "\n"

    output += "profileset.{}_dw_fsc=talents=1223212\n".format(ilvl)
    output += "profileset.{}_dw_fsc+=head=,id=178777,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_fsc+=neck=,id=178827,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_fsc+=shoulders=,id=178820,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_fsc+=back=,id=178851,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_fsc+=chest=,id=180099,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_fsc+=wrists=,id=179354,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_fsc+=legs=,id=178818,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_fsc+=feet=,id=180101,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_fsc+=finger1=,id=178933,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_fsc+=finger2=,id=178736,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_fsc+=trinket1=,id=178769,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_fsc+=trinket2=,id=179342,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_fsc+=main_hand=,id=178730,ilevel={},enchant=rune_of_razorice\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_fsc+=off_hand=,id=179340,ilevel={},enchant=rune_of_the_fallen_crusader\n".format(ilvl, ilvl)
    output += "\n"

    output += "profileset.{}_dw_bos=talents=2223213\n".format(ilvl)
    output += "profileset.{}_dw_bos+=head=,id=178777,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_bos+=neck=,id=178827,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_bos+=shoulders=,id=178820,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_bos+=back=,id=178851,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_bos+=chest=,id=180099,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_bos+=wrists=,id=179354,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_bos+=legs=,id=178818,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_bos+=feet=,id=180101,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_bos+=finger1=,id=178933,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_bos+=finger2=,id=178736,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_bos+=trinket1=,id=178769,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_bos+=trinket2=,id=179342,ilevel={}\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_bos+=main_hand=,id=178730,ilevel={},enchant=rune_of_razorice\n".format(ilvl, ilvl)
    output += "profileset.{}_dw_bos+=off_hand=,id=179340,ilevel={},enchant=rune_of_the_fallen_crusader\n".format(ilvl, ilvl)
    output += "\n"

    return output


with open('full_profile.simc', 'w') as f:
    f.write(output)

    for x in [185, 195, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295, 305, 315, 325, 335, 345, 355, 365, 375]:
        f.write(output_ilvl(x))
