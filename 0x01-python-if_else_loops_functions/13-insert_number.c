#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - insert new node
 * @head: p
 * @number: new node
 *
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux, *p;

	p = malloc(sizeof(listint_t));

	if (!p)
	{
		return (NULL);
	}

	aux = *head;
	p->i = number;
	if (!*head || aux->i > number)
	{
		return (p->next = *head, *head = p, p);
	}
	while (aux->next)
	{
		if (aux->next->i >= number)
		{
			return (p->next = aux->next, aux->next = p, p);
		}
		aux = aux->next;
	}
	p->next = NULL;
	aux->next = p;
	return (p);
}
