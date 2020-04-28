#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - cycle list
 * @list: list
 *
 * Return: 1
 **/
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *a = NULL;

	if (head == NULL)
	{
		return (0);
	}
	while (head != NULL)
	{
		a = head;
		head = head->next;
		if (a <= head)
		{
			return (1);
		}
	}
	return (0);
}
