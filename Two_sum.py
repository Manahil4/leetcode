class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()  # Placeholder for the result list
    current = dummy  # Pointer to build the result list
    carry = 0  # Initialize carry to 0
    
    # Traverse both lists
    while l1 or l2 or carry:
        val1 = (l1.val if l1 else 0)
        val2 = (l2.val if l2 else 0)
        
        # Calculate the sum and carry
        total = val1 + val2 + carry
        carry = total // 10  # Update carry for the next iteration
        total = total % 10  # Get the digit to store in the current node
        
        # Add the result to the new list
        current.next = ListNode(total)
        current = current.next
        
        # Move to the next nodes in the input lists
        if l1: l1 = l1.next
        if l2: l2 = l2.next
        
    return dummy.next  # The first node is a placeholder, so return the next node

# Example usage:
# l1: 2 -> 4 -> 3
# l2: 5 -> 6 -> 4
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

result = addTwoNumbers(l1, l2)
# Output the result linked list
while result:
    print(result.val, end=" -> " if result.next else "")
    result = result.next
# Expected Output: 7 -> 0 -> 8
