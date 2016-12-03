#open spell 
library(readr)
spell_clean <- read_csv("~/Documents/Mobility in Foster Care Children/spell_clean.csv")
View(spell_clean)

#group exits by desirability
ix <- which(spell_clean$EXIT%in% c("XRF","XLC","XRL","XCA") )
ix2 <- which(spell_clean$EXIT%in% c("XOT","XOP","XRM","XRY","XJP") )
ix3 <- which(spell_clean$EXIT%in% c("ZTC","XUK") )

#create new col
spell_clean$ExitReasonDesirability <- "NA"
spell_clean$ExitReasonDesirability[ix] <- "Good"
spell_clean$ExitReasonDesirability[ix2] <- "Bad"
spell_clean$ExitReasonDesirability[ix3] <- "Unknown"
