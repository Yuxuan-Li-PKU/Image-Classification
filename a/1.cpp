(DEFINE result NULL)

(DEFINE (del x lis)
	(COND
		((NULL? lis) result)
		((EQ? (CAR lis) nil) (append(result del(x CDR lis))))
		((EQ? (CAR lis) x) (append(result del(x (CDR lis)))))
		(ELSE (append(append(result (CAR lis)) del(x (CDR lis)))))
		)
	)
)

(DEFINE (append lis1 lis2)
	(COND
		((NULL? lis1) lis2)
		(ELSE (CONS (CAR lis1) 
			(append (CDR lis1) lis2)))
	)
)
