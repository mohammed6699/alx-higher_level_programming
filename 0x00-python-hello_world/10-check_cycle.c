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
	listint_t *node = list;
	listint_t *data = list;

	while (node && data->next)
	{
		data = data->next;
		node = data->next->next;
		if (node == data)
			return (1);
	}
	return (0);
}
