/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 
 
 // Iterative Implementation of reverse linked list
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* prev = NULL;
	struct ListNode* current = head;
	struct ListNode* next;
	
	while(current != NULL){
		next = current->next;
		current-> next = prev;
		prev = current;
		current = next;
	}
	return prev;
}
    
