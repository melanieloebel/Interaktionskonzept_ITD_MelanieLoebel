# Smart City network

The software should enable a patient XY to find a hospital or pharmacy in an easier and faster way. The patient should find the institution which is the closest or which hospital is the most meaningful one. Additinoally the patient should get info about availability and opening hours.

## Requirements

| ID.                    | Description                                                                                                                                                                  |
|:-----------------------|:-------------------------------------------------------------------------------------------------|
| **FR1**                | The system must save user data for each institution (hospitals and pharmacy). 					|
| **FR1.1**              | The system must save the name, adress, phone no. and opening hours. 								|
| **FR2**                | The system must save location for each institutiondata via GPS coordinates.	                    |
| **FR3**              	 | The system must save medical information about the hospital. 							        |
| **FR3.1**              | The system must save the medical specialistic fields.     										|
| **FR3.2**              | The system must save the number of doctors.														|
| **FR3.3**            	 | The system must save number of rooms within each specialistic fields and their status, free or taken.|
| **FR4**              	 | The system must check availibility of doctors. 													|
| **FR4.1**              | The system must get a request for free appointment of a doctor.									|
| **FR4.2**              | The system must send a message with day and time information about the next free apointment.		|
| **FR5**              	 | The system must check availibility of rooms in a medical specialistic field. 					|
| **FR5.1**            	 | The system must get a request for availibility in one medical specialistic field. 				|
| **FR5.2**            	 | The system must send a message how many rooms are free or if there is no room available.			|
|                                                                                                                           |
| **NFR1**              | Usability                                                                                         |
| **NFR1.1**            | Menu item to choose the institution which should be search: Hospital, pharmacy, specialist field. |
| **NFR2**              | Efficiency                                         			                                    |
| **NFR3**              | Performance                                                 			                            |
| **NFR3.1**            | Time for reaction: 1s                                                                             |
| **NFR4**              | Privacy potection                                                                                 |
| **NFR5**              | Safety 				                                                                            |
