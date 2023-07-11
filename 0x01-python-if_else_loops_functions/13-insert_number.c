#include "lists.h"
/**
 * insert_node - insert an element into list
 * @head: head of the list
 * @number: the number to insert in the list
 * Return: new node adress
 */
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *k_new, *k_tmp;

  k_new = malloc(sizeof(listint_t));
  if (k_new == NULL)
    return (NULL);
  k_tmp = *head;
  if (*head == NULL)
    {
      k_new = add_nodeint_end(head, number);
      return (k_new);
    }
  if (k_tmp->n > number)
    {
      k_new->next = k_tmp;
      k_new->n = number;
      *head = k_new;
      return (k_new);
    }
  while (k_tmp->next)
    {
      if (number < k_tmp->next->n)
	{
	  k_new->next = k_tmp->next;
	  k_tmp->next = k_new;
	  k_new->n = number;
	  return (k_new);
	}
      k_tmp = k_tmp->next;
    }
  k_new = add_nodeint_end(head, number);
  return (k_new);
}
