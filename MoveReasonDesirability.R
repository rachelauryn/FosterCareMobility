#first, exit reason desirability (good, bad or unknown) for each spell

library(readr)
spell_clean <- read_csv("~/Documents/Mobility in Foster Care Children/spell_clean.csv") #open spell 

#group exits by desirability
ix <- which(spell_clean$EXIT%in% c("XRF","XLC","XRL","XCA") )
ix2 <- which(spell_clean$EXIT%in% c("XOT","XOP","XRM","XRY","XJP") )
ix3 <- which(spell_clean$EXIT%in% c("ZTC","XUK") )

#create new column
spell_clean$ExitReasonDesirability <- "NA"
spell_clean$ExitReasonDesirability[ix] <- "Good"
spell_clean$ExitReasonDesirability[ix2] <- "Bad"
spell_clean$ExitReasonDesirability[ix3] <- "Unknown"



#second, move reason desirability for every placement, from merged data set (w/o absondence) 

final_merge <- read_csv("~/Documents/Mobility in Foster Care Children/final_merge_minus_absondence.csv")  #open merged data

#group moves by desirability
good <- which(final_merge$CW.Exit.Reason%in% c("**Placed in Facility Foster Home**", 
                                     "**Placement transferred to Second Chance**",  
                                     "Adoption (Ends the Home Removal)", 
                                     "Agency Change - Longer Term Care Needed", 
                                     "College", 
                                     "Discharged to Less Restrictive Placement",  
                                     "Permanent Legal Custodianship (Ends the Home Removal)", 
                                     "Placement in a Pre-Adoptive Home", 
                                     "Placement with Kinship Caregiver", 
                                     "Placement with Siblings", 
                                     "Proximity to Family", 
                                     "Return Home (Ends the Home Removal)") )
bad <- which(final_merge$CW.Exit.Reason%in% c("**Adoption Disrupted**",
                                    "**Child is over 18 and Out of Placement/Court Ordered Closure**", 
                                    "**Independence Achieved**", 
                                    "Death of Child (Ends the Home Removal)", 
                                    "Emancipation (Ends the Home Removal)", 
                                    "Youth is 18+ and No Affidavit/Conciliation", 
                                    "Youth is 18+ and Not in Compliance with Affidavit/Conciliation", 
                                    "Transition to Adult Residential Placement",
                                    "Respite Care Over 7 Days", 
                                    "Placement/Custody by Juvenile Probation", 
                                    "Placement in a Non-Certified Foster Home",  
                                    "Placement Cannot Meet the Child's Behavioral Treatment Needs", 
                                    "Placement Cannot Meet the Child's Medical Treatment Needs", 
                                    "Permanent Placement in the Home of a 'Fit and Willing' Relative (Ends the Home Removal)", 
                                    "**Placed in Group / Residential**", 
                                    "**Placed in Supervised Independent Living**", 
                                    "**Placement Temporarily Unable to Care for Child**", 
                                    "**Reached Age of Majority**", 
                                    "**Youth Voluntarily Left - Independence not Achieved**", 
                                    "Abscondance/Runaway", 
                                    "Agency Contract Ended", 
                                    "Agency Requested Change of Placement",
                                    "Alleged Exposure to Physical or Emotional Harm at this Placement", 
                                    "Child is Hospitalized", 
                                    "Child Requested Change of Placement", 
                                    "Court Ordered (For JPO use only)", 
                                    "Foster Parent Illness/Disability/Death", 
                                    "Foster Parent(s) Requested Change of Placement", 
                                    "Other Permanent Living Arrangement (Ends the Home Removal)", 
                                    "Permanency Planning/Lifetime Connection",  
                                    "**Youth Requires Different Level of Care**") )
contextual <- which(final_merge$CW.Exit.Reason%in% c("Facility Change within Same Provider - Change in Level of Care", 
                                           "Facility Change within Same Provider - Same Level of Care", 
                                           "Change in Facility Foster Home Status", 
                                           "Case Transfer Out of Jurisdiction (Ends the Home Removal)",
                                           "**Placement/Custody to be provided by another agency**", 
                                           "**Placed in CYF Foster Home**") )
#create new column
final_merge$MoveReasonDesirability <- "NA"
final_merge$MoveReasonDesirability[good] <- "Good"
final_merge$MoveReasonDesirability[bad] <- "Bad"
final_merge$MoveReasonDesirability[contextual] <- "Contextual"
