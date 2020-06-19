# Smart City network

The software should enable a patient XY to find a hospital or pharmacy in an easier and faster way. The patient should find the institution which is the closest or which hospital is the most meaningful one. Additinoally the patient should get info about availability and opening hours.

## Requirements

| ID.                    | Description                                                                                                                                                                  |
|:-----------------------|:-------------------------------------------------------------------------------------------------|
| **FR1**                | The system must save user data for each hospital. 												|	
| **FR1.1**              | The system must save the name, total number of free rooms. 											|
| **FR2**                | The system must save location for each hospital via GPS coordinates.	                    		|
| **FR3**              	 | The system must save medical information about the hospital. 							        |
| **FR3.1**              | The system must save the medical specialistic fields.     										|
| **FR3.2**              | The system must save the number of doctors.														|
| **FR3.3**            	 | The system must save number of rooms within each specialistic fields and their status, free or taken.|
| **FR4**              	 | The system must check availibility of doctors. 													|
| **FR4.1**              | The system must get a request for free appointment of a doctor.									|
| **FR4.2**              | The system must check the date which was given as input.											|
| **FR4.2.1**            | The system must check if the input date is an available date (today or in future) and if it is a weekday.|
| **FR4.3**              | The system must send a message which times are available for the respective doctor.				|
| **FR4.4**              | The system must check the time which was given as input.											|
| **FR4.4.1**            | The system must check if the input time for the respective date and doctor is free.				|
| **FR4.5**              | The system must save the appointment with patient name, date and time into the calendar from the respective doctor.|
| **FR4.6**              | The system must send a message info "Accepted appointment".										|
| **FR5**              	 | The system must check availibility of rooms in a medical specialistic field. 					|
| **FR5.1**            	 | The system must get a request for availibility in one medical specialistic field. 				|
| **FR5.2**            	 | The system must send a message how many rooms are free or if there is no room available.			|
|                                                                                                                           |
| **NFR1**              | Usability                                                                                         |
| **NFR1.1**            | Menu item to choose between options like "Show free rooms", "Show specialists" and "Make an appointment".|
| **NFR2**              | Efficiency                                         			                                    |
| **NFR3**              | Performance                                                 			                            |
| **NFR3.1**            | Time for reaction: 1s                                                                             |
| **NFR4**              | Privacy potection                                                                                 |
