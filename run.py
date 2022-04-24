if __name__ == "__main__":
	try:
		__import__("brute").Main()
	except Exception as e:
		exit(str(e))
