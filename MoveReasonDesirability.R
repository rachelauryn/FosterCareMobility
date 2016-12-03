#open spell 
library(readr)
spell_clean <- read_csv("~/Documents/Mobility in Foster Care Children/spell_clean.csv")
View(spell_clean)

#group exits by desirability
ix <- which(spell_clean$EXIT%in% c("XRF","XLC","XRL","XCA") )
ix2 <- which(spell_clean$EXIT%in% c("XOT","XOP","XRM","XRY","XJP") )
ix3 <- which(spell_clean$EXIT%in% c("ZTC","XUK") )

#create new col
spell_clean$MoveReasonDesirability <- "NA"
spell_clean$MoveReasonDesirability[ix] <- "Good"
spell_clean$MoveReasonDesirability[ix2] <- "Bad"
spell_clean$MoveReasonDesirability[ix3] <- "Unknown"
