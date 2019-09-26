namespace ICS.Quantum{
	open Microsoft.Quantum.Intrinsic;
	open Microsoft.Quantum.Canon;
		}
		//Message($There were {maxCount-count} zeros and {count} ones)
	
	

	operation Entangle(): Unit{
		let maxCount = 1000
		mutable q0Zeros = 0;
		mutable qlZeros = 0;
		mutable agree = 0;
		using(qs = Qbit[2]){
			H(qs[0]);
			CNOT(qs[0], qs[1]);
			let r0 = M(qs[0]);
			let r1 = M(qs[1]);
			
			if (r0 == Zero){
				set qlZeros += 1;
			}
}
ResetAll(qs));
}
