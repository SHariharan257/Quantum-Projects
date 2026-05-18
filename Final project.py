import qiskit as q
import qiskit_aer as qa
qc=q.QuantumCircuit(8)
for i in range(8):
    qc.h(i)
qc.measure_all()
print(qc)
simulator=qa.AerSimulator()
compiled=q.transpile(qc,simulator)
val=simulator.run(compiled,shots=1)
res=val.result()
cnt=res.get_counts()
rn=int(list(cnt.keys())[0],2)
length=len(str(rn))
if length<8:
    rn="0"*(8-length)+str(rn)
    print("Your 8 digit otp is :",rn)
