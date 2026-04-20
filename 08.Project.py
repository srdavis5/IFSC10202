
file = open("constitution.txt", "r")
lines = [line.strip() for line in file.readlines()]
file.close()

while True:
    search_term = input("Enter search term: ").strip()
    
    if not search_term:
        break
        
    term_lower = search_term.lower()
    current_line_idx = 0
    
    while current_line_idx < len(lines):
        line = lines[current_line_idx]
        
        if term_lower in line.lower():
            
            start_idx = current_line_idx
            while start_idx > 0 and lines[start_idx - 1] != "":
                start_idx -= 1
                
            end_idx = current_line_idx
            while end_idx < len(lines) - 1 and lines[end_idx + 1] != "":
                end_idx += 1
                
            for i in range(start_idx, end_idx + 1):
                print(f"Line {i + 1}: {lines[i]}")
            print() 
            
            current_line_idx = end_idx 
            
        current_line_idx += 1
