#include "lists.h"

/**
 * insert_node - insert node to a
 * sorted linked list
 * @head: double pointer to linked list
 * @number: number to insert
 *
 * Return: new list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;

	if (*head == NULL)
	{
		(*head) = malloc(sizeof(listint_t));
		if (*head == NULL)
			return (NULL);
		(*head)->n = number;
		(*head)->next = NULL;
		return (*head);
	}
	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	if (number < (*head)->n)
	{
		temp->n = (*head)->n;
		temp->next = (*head)->next;
		(*head)->next = temp;
		(*head)->n = number;
		return (*head);
	}
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		free(temp);
		return (NULL);
	}
	new = *head;
	while (new->next != NULL && (new->next)->n < number)
	{
		new = new->next;
	}
	temp->n = number;
	temp->next = new->next;
	new->next = temp;

	return (*head);
}
