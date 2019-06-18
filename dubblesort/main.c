int __cdecl main(int argc, const char **argv, const char **envp)
{
  unsigned int $eax; // $eax
  int *$edi; // $edi
  unsigned int count; // esi
  int v6; // ecx
  unsigned int count2; // esi
  int v8; // ST08_4
  int result; // $eax
  int v10; // edx
  unsigned int v11; // et1
  unsigned int N; // [esp+18h] [ebp-74h]
  int numbers; // [esp+1Ch] [ebp-70h]
  char buf; // [esp+3Ch] [ebp-50h]
  unsigned int v15; // [esp+7Ch] [ebp-10h]

  v15 = __readgsdword(0x14u);
  sub_8B5();
  printf(1, "What your name :");
  read(0, &buf, 0x40u);
  printf(1, "Hello %s,How many numbers do you what to sort :");
  scanf("%u", &N);
  $eax = N;
  if ( N )
  {
    $edi = &numbers;
    count = 0;
    do
    {
      printf(1, "Enter the %d number : ");
      fflush(stdout);
      scanf("%u", $edi);
      ++count;
      $eax = N;
      ++$edi;
    }
    while ( N > count );
  }
  process(&numbers, $eax);
  puts("Result :");
  if ( N )
  {
    count2 = 0;
    do
    {
      v8 = *(&numbers + count2);
      printf(1, "%u ");
      ++count2;
    }
    while ( N > count2 );
  }
  result = 0;
  v11 = __readgsdword(0x14u);
  v10 = v11 ^ v15;
  if ( v11 != v15 )
    EXIT(v6, v10);
  return result;
}
