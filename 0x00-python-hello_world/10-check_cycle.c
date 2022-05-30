#include "lists.h"

/**
 * check_cycle - check if there is a cycle
 * in a linked list
 * @list: list to be checked
 *
 * Return: 0 if no cycle
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *temp;

	if (list == NULL || list->next == NULL)
		return (0);
	current = list;
	temp = current->next;
	while (current != NULL && temp->next != NULL && temp->next->next != NULL)
	{
		if (current == temp)
			return (1);
		current = current->next;
		temp = temp->next->next;
	}
	return (0);
}
