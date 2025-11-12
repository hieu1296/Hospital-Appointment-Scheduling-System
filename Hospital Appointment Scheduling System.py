import heapq

class Hospital:
    def __init__(self):
        self.doctors = []
        self.patients = []
        

class User:
    def __init__(self, id):
        self.id = id

class Doctor(User):
    def __init__(self, id, start_time, end_time, slot_length):
        super().__init__(id)
        self.start_time = start_time
        self.end_time = end_time
        self.slot_length = slot_length

class Patient(User):
    def __init__(self, id, arrival_time, priority):
        super().__init__(id)
        self.arrival_time = arrival_time
        self.priority = priority


class Solution:

    def Schedule(self, Hospital: Hospital):
        D, P = len(Hospital.doctors), len(Hospital.patients)
        Doctors, Patients = Hospital.doctors, Hospital.patients

        minH = [] # Priority, Arrival_Time
        res = [[-1, -1] for _ in range(P)] # Actually we dont need Res, yinwei we could use the patients data once, Hence why dont we just simply replace it with the result ?
        i = 0


        while (minH or i < P) and Hospital.available_doctors > 0:
            for doctor in Doctors:
                if doctor.start_time >= doctor.end_time:
                    continue

                
                # enqueue patients arriving within this slot window
                while i < P and Patients[i].arrival_time <= doctor.start_time:
                    priority, arrival_time = Patients[i].priority, Patients[i].arrival_time
                    heapq.heappush(minH, (-priority, arrival_time, i))
                    i += 1


                if minH:
                    print(minH, doctor.start_time)
                    priority, arrival_time, idx = heapq.heappop(minH)
                    slot_start = doctor.start_time
                    res[idx] = [doctor.id, slot_start]

                doctor.start_time = doctor.start_time + doctor.slot_length

                if doctor.start_time  >= doctor.end_time:
                    Hospital.available_doctors -= 1
                    # print(i, minH, Hospital.available_doctors )
            print(i, minH, Hospital.available_doctors)
        return res
    
def DataHandle(hospital):
    with open("HospitalDB.txt") as f:
        lines = [line.strip() for line in f if line.strip()]


    D, P = map(int, lines[0].split())
    
    for i in range(1, 1 + D):
        doctor_id, start, end, slot = map(int, lines[i].split())
        doctor = Doctor(doctor_id, start, end, slot)
        print(doctor.id, doctor.start_time, doctor.end_time, doctor.slot_length)
        hospital.doctors.append(doctor)

    for i in range(1 + D, 1 + D + P):
        patient_id, arrival, priority = map(int, lines[i].split())
        patient = Patient(patient_id, arrival, priority)
        print(patient.id, patient.arrival_time, patient.priority)
        hospital.patients.append(patient)

    hospital.available_doctors = len(hospital.doctors)

if __name__ == "__main__":

    sll = Solution()
    hospital = Hospital()
    DataHandle(hospital)
    print(sll.Schedule(hospital))
