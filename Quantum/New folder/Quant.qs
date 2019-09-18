namespace ICS.Quantum{
	open Microsoft.Quantum.Intrinsic;
	open Microsoft.Quantum.Canon;
	
	operation HelloWorld(): Result{
		Message("Hello, World");
		return Zero;
	}
	
	operation Hello(name: String): Unit{
		Message($"Hello, {name}"); //print("Hello, {}" .format(name))
	}
	
	operation HelloSeward(): Result{
		Hello("Mr. Seward");
		return One;
	}
	operation QbitPlay(): Unit{
		using (q=Qbit()){
			if(H(q))=Zero{
				Message("It was zero!");}
			else {
				Message("It was one");}
			} 
			Reset(q);
	}
}
