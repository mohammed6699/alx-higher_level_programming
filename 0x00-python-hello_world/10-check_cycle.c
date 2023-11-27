#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/*
 * check_cycle - function to check the cycle of the list
 * @list: pointer to the list created
 * Return: (0) fail, (1) success
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list, *second = list;

	while (first && first->next)
	{
		second = second->next;
		first = first->next->next;
		if (first == second)
			return (1);
	}
	return (0);
}
