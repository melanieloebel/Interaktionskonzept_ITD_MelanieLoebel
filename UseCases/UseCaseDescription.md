# Use Case description
## Titel:
Search a hospital

## Short description:
Patient select hospital and optionally medical specialistic field for search, check availibility of medical specialistic field (free rooms), save an appointment at a doctor.

## Actuator:
Patient

## Precondition: 
GPS position is availible.
Free appointments are availible.

## Description of operational sequence: 
1. Indentify the GPS position of the patient 
2. Compare hospital GPS data with the GPS data of the patient
3. Show the closest hospitals which have the chosen medical specialistic field
4. Show the doctors for the chosen  medical specialistic field
5. Request for free rooms of the medical specialistic field
6. Request for free appointments for respective doctor.
7. Accept or reject the chosen appointment.

## Effect:
Display of free appointment of the doctor or message "no appointment availible".
Display of the total number of free rooms of the medical specialistic field or message "no room availible".
