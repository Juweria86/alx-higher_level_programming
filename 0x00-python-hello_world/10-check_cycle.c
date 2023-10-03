#include "lists.h"
/**
 * check_cycle - cecks if there is cycle in the list
 * list - list to be checked
 * Return 1 if there is cycle else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
