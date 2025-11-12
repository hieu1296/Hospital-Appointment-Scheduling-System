# Hospital-Appointment-Scheduling-System
College Assignment 

Case A — 1 doctor, emergency arrives after first slot

Input

1 4
1 540 600 15
201 540 0
202 541 0
203 542 1
204 543 0

Case B — 2 doctors, mix of arrivals + one emergency

Input

2 5
1 540 600 15
2 540 600 15
201 530 0
202 540 0
203 541 0
204 555 0
205 559 1

Case C — end=585 (slots 540, 555, 570), emergency at same time as normals

Input

1 3
1 540 585 15
201 540 0
202 540 1
203 540 0

Case D — Unschedulable (only one slot)

Input

1 3
1 540 555 15
201 540 0
202 540 1
203 540 0

Case E — Simple FIFO, no emergencies

Input

1 4
1 540 600 15
201 530 0
202 540 0
203 541 0
204 555 0

Case F — Late arrivals; one arrives at end_time (cannot be scheduled)

Input

1 4
1 540 600 15
201 556 0
202 557 0
203 559 1
204 600 0

Case G — Two doctors, staggered starts

Input

2 4
1 540 600 15
2 555 615 15
201 540 0
202 541 1
203 552 0
204 556 0

Case H — Tie-breaking by doctor_id on same slot time

Input

2 3
1 540 570 15
2 540 570 15
201 540 0
202 540 1
203 540 0
